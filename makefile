CXX=g++
CXXFLAGS=-Wall -g -std=c++11
NAME=zakazany-las
CXXSRC=main.cpp
CXXOBJ=$(CXXSRC:.cpp=.o)

$(NAME): $(CXXOBJ)
	$(CXX) $(CXXFLAGS) $? -o $@
	mv $(NAME) build/

$(CXXOBJ): $(CXXSRC)
	$(CXX) $(CXXFLAGS) -c $*.cpp -o $@

clean:
	rm -f *.o
	rm -f build/$(NAME)