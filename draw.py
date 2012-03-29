import pylab as py





def draw_cechy_3d(cecha_target, cecha_non_target):
    from mpl_toolkits.mplot3d import Axes3D
    fig = py.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(cecha_target[0], cecha_target[1], cecha_target[2],c='r')
    ax.scatter(cecha_non_target[0], cecha_non_target[1], cecha_non_target[2],c='b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    py.show()

def draw_cechy_2d(cecha_target, cecha_non_target):
    py.plot(cecha_non_target[0], cecha_non_target[1], 'bo')
    py.plot(cecha_target[0], cecha_target[1], 'ro')
    py.show()


def draw_signal_matrix(signal_target, signal_non_target, rows=4, columns=5, type='plain'):
    for chan in range(signal_target.shape[1]):
        py.subplot(rows,columns,chan+1)
    
        if type == 'plain':
            non_target_plot = (signal_non_target[:,chan,:]).transpose()
            target_plot = (signal_target[:,chan,:]).transpose()
        elif type == 'var':
            target_plot = np.var(signal_target[:,chan,:], axis=1)
            non_target_plot = np.var(signal_non_target[:,chan,:], axis=1)
    
        py.plot(non_target_plot, 'b')
        py.plot(target_plot,'r')
    py.show()

