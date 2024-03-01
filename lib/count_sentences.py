#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    """The value must be a string."""
    return self._value
  
  @value.setter
  def value(self,value):
    """The value must be a string."""
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    value = self.value
    if not value:
      return 0
    
    for punc_marks in [".", "?", "!"]:
      value = value.replace(punc_marks, "|")
    
    sentences = [sentence for sentence in value.split('|') if sentence]

    return len(sentences)
