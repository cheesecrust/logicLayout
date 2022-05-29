import copy


def printTable(table, mterm):
    for i in table:
        tmp = ' '
        for k in range(len(mterm)):
            for j in i:
                if j == mterm[k]:
                    tmp += j + ' '
                    break
            else:
                tmp += 'X '
        print(tmp)
    print("---------------")


def makeTable(mterm, pi):
    table = [[] for _ in range(len(pi))]

    length = len(mterm[0])
    for i in range(len(pi)):
        for j in range(len(mterm)):
            for k in range(length):
                if(pi[i][k] != mterm[j][k] and pi[i][k] != '2'):
                    break
            else:
                table[i].append(mterm[j])

    return table


def rowD(tabluar):
    newTab = []
    for i in range(len(tabluar)):
        for j in range(len(tabluar)):
            if(i == j):
                continue
            if(set(tabluar[i]).intersection(tabluar[j]) and len(tabluar[i]) < len(tabluar[j])):
                tabluar[i] = []
                newTab.append([])
                break
        else:
            newTab.append(tabluar[i])
    return(newTab)


def colD(tabular, mterm):
    epi = []
    for i in mterm:
        cnt = 0
        num = 0
        for j in range(len(tabular)):
            if i in tabular[j]:
                cnt += 1
                num = j
        if(cnt == 1 and num not in epi):
            epi.append(num)
    return epi


def findepi(mterm, tabular, answer):
    epiList = []
    emptytab = [[] for _ in range(len(tabular))]
    while(1):
        epi = []
        epiIdx = []
        epiIdx = (colD(tabular, mterm))
        newtab = [[] for _ in range(len(tabular))]

        for i in epiIdx:
            epi.append(answer[i])
            for j in range(len(tabular[i])):
                tmp = tabular[i][j]
                for l in range(len(tabular)):
                    for m in range(len(tabular[l])):
                        if(tmp == tabular[l][m]):
                            tabular[l][m] = ''
        for i in range(len(tabular)):
            for j in range(len(tabular[i])):
                if(tabular[i][j] != ''):
                    newtab[i].append(tabular[i][j])
        epiList += epi
        tmp = tabular

        tabular = (rowD(newtab))

        if(tabular == emptytab or tmp == tabular):
            return epiList, tabular


def solution(minterm):
    answer = []
    digit = minterm[0]
    num = minterm[1]
    bit_tmp = [[] for _ in range(digit + 1)]
    mterm = []

    for i in range(2, num + 2):
        result = bin(minterm[i])[2:].zfill(digit)
        index = result.count("1")
        bit_tmp[index].append(result)
        mterm.append(result)

    bit_tmp = [i for i in bit_tmp if len(i)]

    while(len(bit_tmp)):
        pi = [[] for _ in range(len(bit_tmp))]
        combined = [[0 for _ in range(len(bit_tmp[i]))]
                    for i in range(len(bit_tmp))]

        for i in range(len(bit_tmp) - 1):
            for j in range(len(bit_tmp[i])):
                for k in range(len(bit_tmp[i + 1])):
                    token = 0
                    idx = 0
                    for s in range(digit):
                        if bit_tmp[i][j][s] != bit_tmp[i + 1][k][s]:
                            if bit_tmp[i][j][s] == "2":
                                token += 2
                                break
                            elif bit_tmp[i + 1][k][s] == "2":
                                token += 2
                                break
                            elif token:
                                token += 1
                                break
                            token += 1
                            idx = s
                    if token == 1:
                        tmp = bit_tmp[i][j][:idx] + \
                            "2" + bit_tmp[i][j][idx + 1:]
                        if tmp not in pi[i]:
                            pi[i].append(tmp)
                        combined[i][j] = 1
                        combined[i + 1][k] = 1
        for i in range(len(combined)):
            for j in range(len(combined[i])):
                if combined[i][j] == 0 and bit_tmp[i][j] not in answer:
                    answer.append(bit_tmp[i][j])
        check = 0
        for i in range(len(bit_tmp)):
            check += len(bit_tmp[i])
        if check == 0:
            break
        if len(answer) == check:
            break
        pi = [i for i in pi if len(i)]

        bit_tmp = pi
    answer.sort()

    emptytab = [[] for _ in range(len(answer))]
    tabular = (makeTable(mterm, answer))
    printTable(tabular, mterm)

    epi, tabular = (findepi(mterm, tabular, answer))
    printTable(tabular, mterm)

    if(emptytab != tabular):
        oritabulr = copy.deepcopy(tabular)
        for i in range(len(oritabulr)):
            newtab = copy.deepcopy(oritabulr)
            newtab[i] = []
            epi_, tabular = ((findepi(mterm, newtab, answer)))
    try:
        finalepi = ["EPI"] + epi + epi_
    except:
        finalepi = ["EPI"] + epi
    answer += finalepi
    for i in range(len(answer)):
        answer[i] = answer[i].replace("2", "-")

    printTable(tabular, mterm)

    return answer


print(solution([3, 6, 0, 1, 2, 5, 6, 7]))
print(solution([4, 6, 0, 4, 8, 10, 11, 12]))
