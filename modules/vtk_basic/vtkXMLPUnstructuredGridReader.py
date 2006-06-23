# class generated by DeVIDE::createDeVIDEModuleFromVTKObject
from module_kits.vtk_kit.mixins import SimpleVTKClassModuleBase
import vtk

class vtkXMLPUnstructuredGridReader(SimpleVTKClassModuleBase):
    def __init__(self, moduleManager):
        SimpleVTKClassModuleBase.__init__(
            self, moduleManager,
            vtk.vtkXMLPUnstructuredGridReader(), 'Reading vtkXMLPUnstructuredGrid.',
            (), ('vtkXMLPUnstructuredGrid',),
            replaceDoc=True,
            inputFunctions=None, outputFunctions=None)
