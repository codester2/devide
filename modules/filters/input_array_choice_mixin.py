import vtk

class InputArrayChoiceMixin:

    _defaultVectorsSelectionString = 'Default Active Vectors'
    _userDefinedString = 'User Defined'

    def __init__(self):
        self._config.vectorsSelection = self._defaultVectorsSelectionString
        self._config.input_array_names = []
        self._config.actual_input_array = None

    def logic_to_config(self, input_array_filter):
        names = []
        # this is the new way of checking input connections
        if input_array_filter.GetNumberOfInputConnections(0):
            pd = input_array_filter.GetInput().GetPointData()
            if pd:
                # get a list of attribute names
                for i in range(pd.GetNumberOfArrays()):
                    names.append(pd.GetArray(i).GetName())

        self._config.input_array_names = names
                
        inf = input_array_filter.GetInputArrayInformation(0)
        vs = inf.Get(vtk.vtkDataObject.FIELD_NAME())

        self._config.actual_input_array = vs
        
    def config_to_view(self, choice_widget):
        # find out what the choices CURRENTLY are (except for the
        # default and the "user defined")
        choiceNames = []
        ccnt = choice_widget.GetCount()
        for i in range(2,ccnt):
            choiceNames.append(choice_widget.GetString(i))

        names = self._config.input_array_names
        if choiceNames != names:
            # this means things have changed, we have to rebuild
            # the choice
            choice_widget.Clear()
            choice_widget.Append(self._defaultVectorsSelectionString)
            choice_widget.Append(self._userDefinedString)
            for name in names:
                choice_widget.Append(name)

        if self._config.actual_input_array:
            si = choice_widget.FindString(self._config.actual_input_array)
            if si == -1:
                # string not found, that means the user has been playing
                # behind our backs, (or he's loading a valid selection
                # from DVN) so we add it to the choice as well
                choice_widget.Append(self._config.actual_input_array)
                choice_widget.SetStringSelection(self._config.actual_input_array)

            else:
                choice_widget.SetSelection(si)

        else:
            # no vector selection, so default
            choice_widget.SetSelection(0)

    def config_to_logic(self, input_array_filter,
                        array_idx=0, port=0, conn=0):

        if self._config.vectorsSelection == \
               self._defaultVectorsSelectionString:
            # default: idx, port, connection, fieldassociation (points), name
            input_array_filter.SetInputArrayToProcess(
                array_idx, port, conn, 0, None)
            
        else:
            input_array_filter.SetInputArrayToProcess(
                    array_idx, port, conn, 0, self._config.vectorsSelection)

        
        