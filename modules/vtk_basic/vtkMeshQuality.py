# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkMeshQuality(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkMeshQuality(), 'Processing.',
            ('vtkDataSet',), ('vtkDataSet',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)