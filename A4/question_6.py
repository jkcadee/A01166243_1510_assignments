# def test_line_intersect_no_intersection_pos(self):
#     self.assertEqual(None, line_intersect([[0.0, 0.0], [1.0, 3.0]], [[1.0, 0.0], [2.0, 3.0]]))

# def test_line_intersect_coincident_pos(self):
#     self.assertEqual([[0.0, 0.0], [1.0, 3.0]], line_intersect([[0.0, 0.0], [1.0, 3.0]], [[0.0, 0.0], [1.0, 3.0]]))

# def test_line_intersect_one_intersect_pos(self):
#     self.assertEqual([0.25, 0.75], line_intersect([[0.0, 0.0], [1.0, 3.0]], [[1.0, 0.0], [0.0, 1.0]]))

# def test_line_intersect_no_intersection_negative(self):
#     self.assertEqual(None, line_intersect([[-1.0, -1.0], [-2.0, -3.0]], [[-2.0, -1.0], [-3.0, -3.0]]))

# def test_line_intersect_coincident_negative(self):
#     self.assertEqual([[-1.0, -1.0], [-2.0, -3.0]], line_intersect([[-1.0, -1.0], [-2.0, -3.0]], [[-1.0, -1.0],
#                       [-2.0, -3.0]]))

# def test_line_intersect_one_intersect_negative(self):
#     self.assertEqual([-1.0, -1.0], line_intersect([[-1.0, -1.0], [-2.0, -3.0]], [[-2.0, -1.0], [-1.0, -1.0]]))
