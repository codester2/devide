# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkMCubesReader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkMCubesReader(), 'Reading vtkMCubes.',
            (), ('vtkMCubes',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
