from pprint import pprint
import re

mammoth = "We have seen thee, queen of cheese, Lying quietly at your ease, Gently fanned by evening breeze, Thy fair form no flies dare seize. All gaily dressed soon you'll go To the great Provincial show, To be admired by many a beau In the city of Toronto. Cows numerous as a swarm of bees, Or as the leaves upon the trees, It did require to make thee please, And stand unrivalled, queen of cheese. May you not receive a scar as We have heard that Mr. Harris Intends to send you off as far as The great world's show at Paris. Of the youth beware of these, For some of them might rudely squeeze And bite your cheek, then songs or glees We could not sing, oh! queen of cheese. We'rt thou suspended from balloon, You'd cast a shade even at noon, Folks would think it was the moon About to fall and crush them soon."

pprint(mammoth)
print(re.findall(r"\bc\w{3}\b",mammoth)) # все четырехбуквенные слова, начинающиеся на c
print(re.findall(r"\bc\w*\b",mammoth)) # все слова, начинающиеся на c
print(re.findall(r"\b\w*r\b",mammoth)) # все слова, заканчивающиеся на r
print(re.findall(r"\b\w*[eyuioaEYUIOA]{3}\S*+\b",mammoth)) # слова, в которых три гласные буквы подряд