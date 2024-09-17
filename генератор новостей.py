# "FAKE NEWS GENERATOR"
from random import choice as cs
source = ["Daily Telegraph", "NewYork Times", "Moscow Times", "Gardian", "BBC", "Washington Post", "Daily Mail", "Novosty Tambova", "Alabuga Daily", "Komsomolskaya Pravda", "TASS"]
rep = ["reported", "said", "announced", "noted", "rumored", "broadcast"]
subject = ["I", "you", "he", "she", "it", "my dog", "your cat", "this man", "Santa Claus", "that girl", "Mr. Armstrong", "Prince Harry"]
verb = ["found", "waited", "shocked", "hit", "kicked", "kissed", "loved", "run over", "called", "touched", "thanked", "informed", "overcame", "congratulated", "chased", "chose", "taught", "sponsored"]
adjective = ["old", "young", "talanted", "generous", "illiterate", "capricious", "stupid", "smart", "amazing", "procrastinating", "talkative", "agile", "fashionable", "unpredictabel", "cool", "funny", "slim", "fat", "stabborn", "lazy"]
object1 = ["mouse", "neighbour", "shop assistant", "D'Artagnan", "creditor", "engineer", "actor", "artist", "Albert Einstein", "Ms. Silvia", "Alexander Pushkin", "Abraham Lincoln", "Christopher Columbus", "director", "programmer"]
time1 = ["an hour ago", "yesterday", "last evening", "last Monday", "last Tuesday", "last Wednesday", "last Thursday", "last Friday", "last Saturday", "last Sunday", "a month ago", "last year", "yesterday morning", "ten years ago", "last year"]
print("!!!SENSATIONAL NEWS!!!")
key = " "
while key != "-":
#   print('{0} {1} that {2} {3} {4} {5} {6}.'.format(cs(source), cs(rep), cs(subject), cs(verb), cs(adjective), cs(object1), cs(time1)))
    print(f'{cs(source)} {cs(rep)} that {cs(subject)} {cs(verb)} {cs(adjective)} {cs(object1)} {cs(time1)}.')
    print()
    key = input('To get more news press "Enter". For exit input "-"')
    print()