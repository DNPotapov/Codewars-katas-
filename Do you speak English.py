'''
Do you speak "English"? (8 kyu)
https://www.codewars.com/kata/58dbdccee5ee8fa2f9000058
'''

def sp_eng(sentence):
    sentence = sentence.lower()
    return True if "english" in sentence else False