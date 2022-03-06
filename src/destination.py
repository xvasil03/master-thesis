
import abc
import json

from pystalkd.Beanstalkd import Connection as BeanstalkdConnection

def get_destination_class_name(destination):
    return destination.title() + "Destination"

class DestinationI(object, metaclass=abc.ABCMeta):
    def __init__(self, conf):
        raise NotImplementedError('__init__ is not implemented')

    def send_notification(self, notification):
        raise NotImplementedError('send_notification is not implemented')

class BeanstalkdDestination(DestinationI):
    def __init__(self, conf):
        self.conf = conf
        self.connection = BeanstalkdConnection(self.conf["addr"], self.conf["port"]) #todo tube

    def send_notification(self, invoking_configuration, notification):
        self.connection.put(json.dumps(notification))