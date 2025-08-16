from app.LogicCommandsFactory import LogicCommandsFactory
from app.OrderCommandsFactory import OrderCommandsFactory
from app.MarionetteCommandsFactory import MarionetteCommandsFactory


class FactoryHub:

    def __init__(self):
        self.marionette_commands_factory = MarionetteCommandsFactory()
        self.logic_commands_factory = LogicCommandsFactory()
        self.order_commands_factory = OrderCommandsFactory()


    def for_marionette_commands(self):
        return self.marionette_commands_factory
    
    def for_logic_commands(self):
        return self.logic_commands_factory
    
    def for_order_commands(self):
        return self.order_commands_factory
