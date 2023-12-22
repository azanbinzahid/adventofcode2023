def read(filename='in.txt'):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data
    

class Configuration:
    def __init__(self):
        self.modules = {}

    def add_module(self, module):
        self.modules[module.id] = module

    def get_module(self, id):
        if id not in self.modules:
            module = Module(id)        
            self.modules[id] = module
        return self.modules[id]

class Pulse:
    low = 'low'
    high = 'high'

class Module():
    def __init__(self, id):
        self.id = id
        self.on = None
        self.type = None
        self.pulse = None
        self.destinations = []
        self.inputs = {}
        self.low_count = 0
        self.high_count = 0
        self.pulse_queue = []

    def add_destination(self, destination):
        self.destinations.append(destination)

    def process_pulse(self):
        while len(self.pulse_queue):
            module, pulse = self.pulse_queue.pop(0)
            module.receive_pulse(self, pulse)

    def send_pulse(self, pulse):
        for d in self.destinations:
            self.low_count += 1 if pulse == Pulse.low else 0
            self.high_count += 1 if pulse == Pulse.high else 0

            print(f"{self.id} -> {pulse} -> {d.id}")

            self.pulse_queue.append((d, pulse))
            # d.receive_pulse(self, pulse)

    # @abstractmethod
    def receive_pulse(self, module, pulse):
        pass

    def display(self):
        print(f"id: {self.id}")
        print(f"on: {self.on}")
        print(f"low count: {self.low_count}")
        print(f"high count: {self.high_count}")
        print(f"pulse: {self.pulse}")
        print("destinations")
        for m in self.destinations:
            print(m.id)
        print("inputs")
        for k, v in self.inputs.items():
            print(f"{k} -> {v}")
        print("===")


class FlipFlop(Module):
    def __init__(self, id):
        Module.__init__(self, id)
        self.on = False 
        self.pulse = Pulse.low

    def receive_pulse(self, module_id, pulse):
        if pulse == Pulse.high:
            return
        elif pulse == Pulse.low:
            if self.on:
                self.on = False
                self.send_pulse(Pulse.low)
            else:
                self.on = True
                self.send_pulse(Pulse.high)

class Conjunction(Module):
    def __init__(self, id):
        Module.__init__(self, id)
        self.type = 'Conjunction'
 
    def add_input(self, input):
        self.inputs[input.id] = Pulse.low

    def receive_pulse(self, module, pulse):
        # only update which it is tracking
        # if module.id not in self.inputs:
        #     self.inputs[module.id] = 

        self.inputs[module.id] = pulse
        all_high = all(self.inputs[m] == Pulse.high for m in self.inputs.keys())
        if all_high:
            self.send_pulse(Pulse.low)
        else:
            self.send_pulse(Pulse.high)
    
class Broadcast(Module):
    def receive_pulse(self, module, pulse):
        self.send_pulse(pulse)

class Button(Module):
    pass

def make_class(pulses, config):
    # make flip flop module
    for pulse in pulses:
        if '%' in pulse:
            name = pulse.split('->')[0][1:].strip()
            module = FlipFlop(name)
            config.add_module(module)

        # make conjuction module
        if '&' in pulse:
            name = pulse.split('->')[0][1:].strip()
            module = Conjunction(name)
            config.add_module(module)

    # add connections
    for pulse in pulses:
        if 'broadcast' in pulse:
            modules = pulse.split('->')[1].split(',')
            module = Broadcast('broadcaster')
            for m in modules:
                m = m.strip()
                module.add_destination(config.get_module(m))
            config.add_module(module)

            # add button
            button = Button('button')
            button.add_destination(module)
            config.add_module(button)
        
        elif '&' in pulse:
            modules = pulse.split('->')[1].split(',')
            module = config.get_module(pulse.split('->')[0][1:].strip())
            for m in modules:
                m = config.get_module(m.strip())
                module.add_destination(m)
                # if m.type == 'Conjunction':
                #     m.add_input(module)

        elif '%' in pulse:
            modules = pulse.split('->')[1].split(',')
            module = config.get_module(pulse.split('->')[0][1:].strip())
            for m in modules:
                m = config.get_module(m.strip())
                module.add_destination(m)
                if m.type == 'Conjunction':
                    m.add_input(module)


if __name__ == "__main__":

    pulses = read()
    config = Configuration()
    make_class(pulses, config)

    button = config.get_module('button')
    for module in config.modules.values():
        print(module.display())

    for i in range(1000):
        low = 0
        high = 0
        button.send_pulse(Pulse.low)

        pulse_count = True
        while pulse_count:
            pulse_count = False
            for module in config.modules.values():
                if len(module.pulse_queue) > 0:
                    pulse_count = True
                    module.process_pulse()
   
        for module in config.modules.values():
            low += module.low_count
            high += module.high_count

        print(low, high)
        print("-------\n")
        if i == 999:
            print(low*high) 

    # print("--======--")
    # print("\n")
    # print("--======--")
    # for module in config.modules.values():
    #     print(module.display())