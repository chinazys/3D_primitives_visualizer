from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.line.line import Line
import numpy as np


class rotate_surface(Primitive):
    plots = []

    def __init__(self, base: Curve, dot: list, vector: list):  # line= dot P(a,b,c) + vector s(n,m,p)    (P in curve)

        if vector == [0, 0, 0]:
            raise Exception('vector is invalid = [0,0,0]')
        assert len(dot) == 3, "dot is invalid"
        assert len(vector) == 3, "vector is invalid"

        self.base = base
        self.base.build()

        self.dot = dot

        self.vector = vector

        # self.main_line = Line([dot, vector + dot])

        # self.main_line.build()

        self.x_list, self.y_list, self.z_list = [], [], []

    def build(self):

        def rotate_point_about_line(point, line_point, line_direction, angle):
            # Convert angle to radians
            theta = np.radians(angle)

            # Convert all inputs to numpy arrays for consistency
            point = np.array(point)
            line_point = np.array(line_point)
            line_direction = np.array(line_direction)

            # Calculate unit direction vector
            u = line_direction / np.linalg.norm(line_direction)

            # Calculate rotation matrix
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            u_x = u[0]
            u_y = u[1]
            u_z = u[2]
            rot_mat = np.array([[cos_theta + u_x ** 2 * (1 - cos_theta), u_x * u_y * (1 - cos_theta) - u_z * sin_theta,
                                 u_x * u_z * (1 - cos_theta) + u_y * sin_theta],
                                [u_y * u_x * (1 - cos_theta) + u_z * sin_theta, cos_theta + u_y ** 2 * (1 - cos_theta),
                                 u_y * u_z * (1 - cos_theta) - u_x * sin_theta],
                                [u_z * u_x * (1 - cos_theta) - u_y * sin_theta,
                                 u_z * u_y * (1 - cos_theta) + u_x * sin_theta,
                                 cos_theta + u_z ** 2 * (1 - cos_theta)]])

            # Apply rotation to point
            rotated_point = np.matmul(rot_mat, (point - line_point)) + line_point

            return rotated_point.tolist()

        a, b, c = self.dot
        m, n, p = self.vector

        # ax=self.main_line.plot(ax)

        x = self.base.x_list
        y = self.base.y_list
        z = self.base.z_list

        x_new, y_new, z_new = [], [], []
        x_, y_, z_ = [], [], []

        for j in range(0, 366):
            for i in range(0, len(x)):
                theta = j
                x_rot, y_rot, z_rot = rotate_point_about_line(np.array([x[i], y[i], z[i]]), np.array([a, b, c]),
                                                         np.array([m, n, p]), theta)
                x_new.append(x_rot)
                y_new.append(y_rot)
                z_new.append(z_rot)
            x_.append(x_new)
            y_.append(y_new)
            z_.append(z_new)
            x_new, y_new, z_new = [], [], []



        self.x_list = np.array(x_)
        self.y_list = np.array(y_)
        self.z_list = np.array(z_)

    def plot(self, ax, canvas, fig):
        from matplotlib.animation import FuncAnimation

        # self.main_line.plot()
        # self.base.plot()

        # self.build()

        t = np.linspace(-50, 50, 100)
        a, b, c = self.dot
        m, n, p = self.vector
        x_line = a + m * t
        y_line = b + n * t
        z_line = c + p * t
        self.plots.append(ax.plot(x_line, y_line, z_line))
        self.plots.append(ax.plot(self.base.x_list, self.base.y_list, self.base.z_list))
        self.plots.append(ax.plot_surface(self.x_list, self.y_list, self.z_list, color='b'))
        # anim = FuncAnimation(fig, animate, frames=self.LENGTH + 1, repeat=False, interval=self.INTERVAL)

        canvas.draw()