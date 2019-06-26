# Create a new class, SMS_store.
# The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:
#
# my_inbox = SMS_store()
# This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages).
# Each message will be represented as a tuple:
#
# (has_been_viewed, from_number, time_arrived, text_of_SMS)
# The inbox object should provide these methods:
#
# my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
#   # Makes new SMS tuple, inserts it after other messages
#   # in the store. When creating this message, its
#   # has_been_viewed status is set False.
#
# my_inbox.message_count()
#   # Returns the number of sms messages in my_inbox
#
# my_inbox.get_unread_indexes()
#   # Returns list of indexes of all not-yet-viewed SMS messages
#
# my_inbox.get_message(i)
#   # Return (from_number, time_arrived, text_of_sms) for message[i]
#   # Also change its state to "has been viewed".
#   # If there is no message at position i, return None
#
# my_inbox.delete(i)     # Delete the message at index i
# my_inbox.clear()       # Delete all messages from inbox
# Write the class, create a message store object, write tests for these methods, and implement the methods.

from unit_tester import test


class SMS_store:

    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        self.messages.append( (False, from_number, time_arrived, text_of_sms) )

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        indexlist = []
        for i in self.messages:
            if i[0] is False:
                indexlist.append(self.messages[i])
        return indexlist

    def get_message(self, i):
        message = self.messages[i]
        readmessage = (True, message[1], message[2], message[3])
        self.messages[i] = readmessage
        return message

    def delete(self, i):
        self.messages.remove(self.messages[i])
        return self.messages

    def clear(self):
        self.messages = []
        return self.messages


my_inbox = SMS_store()
my_inbox.add_new_arrival(12345, "12:00", "Hello World!")
test(my_inbox.message_count()==1)
print(my_inbox.get_message(0))