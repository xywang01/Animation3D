import numpy as np


def view_matrix_3d(_azimuth, _elevation):
    """ A view matrix, directly borrowed from MatLab's function viewmtx. This only implements the
     orthographical version """
    # only takes int
    if not isinstance(_azimuth, int):
        _azimuth = int(np.floor(_azimuth))
    if not isinstance(_elevation, int):
        _azimuth = int(np.floor(_elevation))
    # make sure data is in the correct range
    # elevation should be between -180 and 180
    _elevation = (((_elevation + 180) % 360) + 360) % 360 - 180
    if _elevation > 90:
        _elevation = 180 - _elevation
        _azimuth += 180
    elif _elevation < -90:
        _elevation = -180 - _elevation
        _azimuth += 180
    # azimuth should be between 0 and 360
    _azimuth = ((_azimuth % 360) + 360) % 360

    _azimuth = np.deg2rad(_azimuth)
    _elevation = np.deg2rad(_elevation)

    # view transformation matrix
    trans_mat = np.array([
        [np.cos(_azimuth), np.sin(_azimuth), 0., 0.],
        [-np.sin(_elevation) * np.sin(_azimuth), np.sin(_elevation) * np.cos(_azimuth), np.cos(_elevation), 0.],
        [np.cos(_elevation) * np.sin(_azimuth), -np.cos(_elevation) * np.cos(_azimuth), np.sin(_elevation), 0.],
        [0.,                                     0.,                                    0.,                 1.]
    ], dtype=np.float64)

    return trans_mat
