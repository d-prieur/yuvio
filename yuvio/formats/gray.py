from abc import ABC
import numpy as np
from .. import pixel_formats
from ..core import Format


class _GrayBase(Format, ABC):
    """Base for all gray/yuv400 formats."""
    @staticmethod
    def chroma_subsampling():
        return 0, 0

    def unpack(self, data):
        y = data['y']
        return y, None, None

    def pack(self, yuv):
        data = np.empty(yuv[0].shape[0], dtype=self.dtype)
        data['y'][:] = yuv[0]
        return data


class Gray(_GrayBase):
    @staticmethod
    def identifier():
        return "gray"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '<u1', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray10LE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray10le"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '<u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray10BE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray10be"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '>u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray16LE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray16le"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '<u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray16BE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray16be"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '>u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray9LE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray9le"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '<u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray9BE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray9be"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '>u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray12LE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray12le"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '<u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray12BE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray12be"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '>u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray14LE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray14le"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '<u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


class Gray14BE(_GrayBase):
    @staticmethod
    def identifier():
        return "gray14be"

    @property
    def dtype(self):
        return np.dtype([
            ('y', '>u2', (self._height, self._width)),
            ('u', '|V0'),
            ('v', '|V0')
        ])


pixel_formats.register(Gray)
pixel_formats.register(Gray10LE)
pixel_formats.register(Gray10BE)
pixel_formats.register(Gray16LE)
pixel_formats.register(Gray16BE)
pixel_formats.register(Gray9LE)
pixel_formats.register(Gray9BE)
pixel_formats.register(Gray12LE)
pixel_formats.register(Gray12BE)
pixel_formats.register(Gray14LE)
pixel_formats.register(Gray14BE)
