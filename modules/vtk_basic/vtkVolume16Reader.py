# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkVolume16Reader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkVolume16Reader(), 'Reading vtkVolume16.',
            (), ('vtkVolume16',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)