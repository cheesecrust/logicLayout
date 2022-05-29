# logicLayout

#row dominance 와 coloum dominace의 구현

우선 row dominance 와 coloum dominance 를 구현하기에 앞서서 우리가 잘 파악 할 수 있도록 표의 형태, 즉 2차원 배열로 minterm 을 pi 별로 구분을 하여 넣어주었다. 

#1.coloum dominance는 위의 작성된 table을 바탕으로 적은 minterm, 지배되는 열을 판단하고 이에 하나의 minterm 만을 가지고 있다면, 이에 해당하는 행을 epi 라고 판단하고, 이를 epi 배열에 넣고
이 행 안에 포함되는 minterm 들을 지워 주었다.

#2.row dominance 는 위의 table 에 coloum dominace 를 한번 진행한 후에 진행 하며 하나의 행이 다른 행을 포함하게 된다면, 포함되는 행은 볼 필요가 없다고 판단하여 지워 주었다.

#3.petric method 위의 coloum dominance 와 row dominance 를 번갈아가며 반복하여 계속 진행시켜서 만약 table 이 비게 되면 멈추고 그대로 종료를 시켜주었다.
하지만 진행을 하는데 더 이상 지워지는 게 없다면 petric method 를 사용하였다. 이는 pi 하나를 고정시킨 후에 위의 row, coloum dominance 를 활용하여 table을 다 비울 때 까지 진행하였다.

