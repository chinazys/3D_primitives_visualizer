from primitives.curve.curve import Curve
from primitives.primitive import Primitive
from primitives.line.line import Line
import numpy as np


class rotate_surface(Primitive):

    def __init__(self, base: Curve, dot: list, vector: list):  # line= dot P(a,b,c) + vector s(n,m,p)    (P in curve)

        if vector == [0, 0, 0]:
            raise Exception('vector is invalid = [0,0,0]')
        assert len(dot) == 3, "dot is invalid"
        assert len(vector) == 3, "vector is invalid"

        self.base = base
        self.base.build()

        self.dot = dot

        self.vector = vector

        #self.main_line = Line([dot, vector + dot])

        #self.main_line.build()

        self.x_list, self.y_list, self.z_list = [], [], []

    def build(self):

        def rotate_around_line(point, line_point, line_direction, angle):

            shifted_point = point - line_point

            direction = line_direction / np.linalg.norm(line_direction)

            v = np.cross([0, 0, 1], direction)
            c = np.dot([0, 0, 1], direction)
            s = np.linalg.norm(v)
            vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
            rotation_matrix = np.eye(3) + vx + np.dot(vx, vx) * ((1 - c) / s ** 2)

            theta = np.radians(angle)
            cos_theta = np.cos(theta)
            sin_theta = np.sin(theta)
            rotation_matrix_z = np.array([[cos_theta, -sin_theta, 0], [sin_theta, cos_theta, 0], [0, 0, 1]])
            rotated_point = np.dot(rotation_matrix_z, np.dot(rotation_matrix, shifted_point))

            rotated_point = np.dot(np.linalg.inv(rotation_matrix), rotated_point)

            rotated_point += line_point

            return rotated_point



        a, b, c = self.dot
        m, n, p = self.vector
        #ax=self.main_line.plot(ax)

        x = self.base.x_list
        y = self.base.y_list
        z = self.base.z_list



        x_new, y_new, z_new = [], [], []
        x_, y_, z_ = [], [], []
        for i in range(len(x)):
            for j in range(0, 366,36):
                theta = j
                x_rot, y_rot, z_rot = rotate_around_line(np.array([x[i], y[i], z[i]]), np.array([a, b, c]),
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

        #self.main_line.plot()
        #self.base.plot()


        #self.build()

        t = np.linspace(-5, 5, 100)
        a, b, c = self.dot
        m, n, p = self.vector
        x_line = a + m * t
        y_line = b + n * t
        z_line = c + p * t
        ax.plot(x_line, y_line, z_line)
        # print(self.x_list,self.z_list,self.y_list)
        ax.plot(self.base.x_list, self.base.y_list, self.base.z_list)
        ax.plot_surface(self.x_list, self.y_list, self.z_list, color='b')
        #anim = FuncAnimation(fig, animate, frames=self.LENGTH + 1, repeat=False, interval=self.INTERVAL)

        canvas.draw()
