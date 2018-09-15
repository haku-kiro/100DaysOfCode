# this file will be the caller for our specialized progression methods
# contains 'unit' tests

import SpecializedProgressionsClass # contains our classes
import progressionClass

# this is done more for - if it was in our logic class file and that was run it would run
# but if it was used in a diff file, this wouldn't run.
# used for unit tests. Not useful here though

if __name__ == '__main__':
    print('Default progression:')
    progressionClass.Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    SpecializedProgressionsClass.ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progresion with increment 5 and start 2:')
    SpecializedProgressionsClass.ArithmeticProgression(5, 2).print_progression(10)

    print('Geometric progression with default base:') # basically binary - nice
    SpecializedProgressionsClass.GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    SpecializedProgressionsClass.GeometricProgression(base=3).print_progression(10)

    print('Fibonacci progression with default start values: ')
    SpecializedProgressionsClass.FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6: ')
    SpecializedProgressionsClass.FibonacciProgression(first=4, second=6).print_progression(10)