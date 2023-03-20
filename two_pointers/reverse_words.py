# Given a sentence, reverse the order of its words without affecting 
# the order of letters within a given word.

def reverse_words(sentence):
   # write you code
   sentences = sentence.split()
   start = 0
   end = len(sentences) - 1
   while (start<end):
      temp = sentences[start]
      sentences[start] = sentences[end]
      sentences[end] = temp
      start += 1
      end -= 1

   reversed_s = ' '.join(sentences)
   return reversed_s
   
tests = ["We love Python", "To be or not to be", "You are amazing"]

for test in tests:
    print(f"input : {test}, output: {reverse_words(test)}")