import methods
from unittest import TestCase



class TryTesting(TestCase):
    def test_square_area_with_side_equal_one(self):
        self.assertEqual(1, methods.square_area(1))

    def test_triangle_area_with_side_equal_two(self):
        self.assertEqual(2,methods.triangle_area(2,2))

    def test_circle_area_with_side_equal_two(self):
        self.assertEqual(12.566370614359172,methods.circle_area(2))

    def test_cylinder_area_with_side_equal_two(self):
        self.assertEqual(50.26548245743669,methods.cylinder_area(2,2))
    
    def test_cylinder_volume_with_side_equal_two(self):
        self.assertEqual(25.132741228718345,methods.cylinder_volume(2,2))

    def test_cube_area_with_side_equal_three(self):
        self.assertEqual(54,methods.cube_area(3))

    def test_cube_volume_with_side_equal_three(self):
        self.assertEqual(27,methods.cube_volume(3))

    def test_cuboid_area_with_side_equal_two(self):
        self.assertEqual(24,methods.cuboid_area(2,2,2))

    def test_cuboid_volume_with_side_equal_two(self):
        self.assertEqual(8,methods.cuboid_volume(2,2,2))


myTest=TryTesting()
myTest.test_square_area_with_side_equal_one()
myTest.test_triangle_area_with_side_equal_two()
myTest.test_circle_area_with_side_equal_two()
myTest.test_cylinder_area_with_side_equal_two()
myTest.test_cylinder_volume_with_side_equal_two()
myTest.test_cube_area_with_side_equal_three()
myTest.test_cube_volume_with_side_equal_three()
myTest.test_cuboid_area_with_side_equal_two()
myTest.test_cuboid_volume_with_side_equal_two