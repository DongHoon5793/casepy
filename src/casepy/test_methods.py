from .simple_methods import *
from .permutation_generator import *


class BinaryGenerator(PermutationGenerator):
    def __init__(self) -> None:
        super().__init__()

    def set_parameters(self, in_number_of_one):
        self.in_number_of_one = in_number_of_one
        element_list = []
        for i in range(in_number_of_one + 1):
            if i < in_number_of_one:
                element_list.append(1)
            else:
                element_list.append(0)
        super().set_parameters(in_number_of_one, element_list)

    def i_case(self, in_iterator: int) -> list:
        element_list = []

        additional_zero = 0
        buff_iterator = in_iterator + 1
        buff_remain = 0

        # 0,0 / 1,1 / 2,1 / 3,2 / 4,2 / 5,2 / 6,2 / 7,3 / 8,3 / 9,3 / 10,3 / 11,3 / 12,3 / 13,3 / 14,3 / 15,4
        while True:
            buff_remain = buff_iterator % 2

            if buff_iterator > 1:  # or buff_remain == 1:
                additional_zero += 1
            else:
                break

            buff_iterator //= 2

        for i in range(self.in_number_of_one + additional_zero, 0, -1):
            if i <= self.in_number_of_one:
                element_list.append(1)
            else:
                element_list.append(0)

        super().set_parameters(self.in_number_of_one + additional_zero, element_list)
        print(
            "//////",
            in_iterator,
            self.in_number_of_one + additional_zero,
            self.element_list,
        )
        for i in range(in_iterator):
            print(2**additional_zero, i, " => ", super().i_case(2**additional_zero - i))
        return super().i_case(in_iterator)
        result = []
        pass

    def case_to_i(self, in_case: list) -> int:
        pass
