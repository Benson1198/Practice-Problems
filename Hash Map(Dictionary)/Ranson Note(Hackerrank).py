def checkMagazine(magazine, note):
    word_dict = {}

    for i in magazine:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] += 1

    for i in note:
        if i in word_dict:
            if word_dict[i] >0:
                word_dict[i] -= 1
            else:
                return 'No'
        else:
            return 'No'

    return 'Yes'
