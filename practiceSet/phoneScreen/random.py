#Printers printing string messages for fortune cookies call an API and try to print a string message randomly. How would you implement this API and keep the responses random?
#Now what if you wanted a weighted response? (Eg. Given 3 string messages, you want the API to return messages 1, 2 and 3 in the ratio 1:2:5). How would you optimize if the API is being invoked repeatedly?

from random import randint

class Solution:

  #Random no repeats
  def random(message):
    array = []
    for i in range(len(message)):
      array.append(i)
    return array

  def message_dict(message):
    message_dict = {}
    for i in range(len(message)):
      message_dict[i] = message[i]
    return message_dict

  def pick_message(message_dict):
    random = randint(0, len(message_dict)):
      return message_dict[random]


  #Weighted randomness
  def w_random(messages, weight):
    total_parts = reduce(lambda x, y: x + y, weight)
    for number in weight:

  #Fill each message with something

  #Might be a better way to improve this
  def w_random_array(weight):
    count_array = []
    counter = 0
    for number in weight:
      count = 0
      while counter < number:
        count_array.append(counter)
        count += 1
      counter += 1
    return count_array

  def w_picker(message, weight_array)
    random = randint(0, len(weight_array))
    return message[random]
