CC=g++
INPUT=5 10 5 10

all: week1 week2

week1: normal_rv_max2.cpp
	@${CC} normal_rv_max2.cpp -o week1.out
	./week1.out ${INPUT}
	@rm week1.out

week2: normal_rv_max_three_moments.cpp
	@${CC} normal_rv_max_three_moments.cpp -o normal_rv_max_three_moments.out
	./normal_rv_max_three_moments.out ${INPUT}
	@rm normal_rv_max_three_moments.out


clean:
	rm -rf *.out
