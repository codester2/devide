#!/usr/bin/env python
# generated by wxGlade 0.2.1 on Fri Feb  7 18:13:59 2003

from wxPython.wx import *

class dicomRDRViewFrame(wxFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: dicomRDRViewFrame.__init__
        kwds["style"] = wxCAPTION|wxMINIMIZE_BOX|wxMAXIMIZE_BOX|wxSYSTEM_MENU|wxRESIZE_BORDER
        wxFrame.__init__(self, *args, **kwds)
        self.viewFramePanel = wxPanel(self, -1)
        self.label_1_copy_copy = wxStaticText(self.viewFramePanel, -1, "DICOM Directory")
        self.DIRNAME_TEXT_ID  =  wxNewId()
        self.dirname_text = wxTextCtrl(self.viewFramePanel, self.DIRNAME_TEXT_ID , "")
        self.BROWSE_BUTTON_ID  =  wxNewId()
        self.browse_button = wxButton(self.viewFramePanel, self.BROWSE_BUTTON_ID , "Browse...")
        self.label_4_copy_copy = wxStaticText(self.viewFramePanel, -1, "Series Instance Index")
        self.SI_IDX_ID  =  wxNewId()
        self.si_idx_spin = wxSpinCtrl(self.viewFramePanel, self.SI_IDX_ID , "0", min=0, max=100, style=wxSP_ARROW_KEYS)
        self.label_1 = wxStaticText(self.viewFramePanel, -1, "Maximum")
        self.seriesInstancesText = wxTextCtrl(self.viewFramePanel, -1, "", style=wxTE_READONLY)
        self.label_5_copy_copy_copy = wxStaticText(self.viewFramePanel, -1, "UID")
        self.si_uid_text = wxTextCtrl(self.viewFramePanel, -1, "", style=wxTE_READONLY|wxHSCROLL)
        self.label_9_copy_copy = wxStaticText(self.viewFramePanel, -1, "Study Description:")
        self.study_description_text = wxTextCtrl(self.viewFramePanel, -1, "", style=wxTE_READONLY|wxHSCROLL)
        self.label_10_copy_copy = wxStaticText(self.viewFramePanel, -1, "Referring Physician:")
        self.referring_physician_text = wxTextCtrl(self.viewFramePanel, -1, "", style=wxTE_READONLY|wxHSCROLL)
        self.label_11_copy_copy = wxStaticText(self.viewFramePanel, -1, "Dimensions:")
        self.dimensions_text = wxTextCtrl(self.viewFramePanel, -1, "", style=wxTE_READONLY|wxHSCROLL)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: dicomRDRViewFrame.__set_properties
        self.SetTitle("vtk_dicom_rdr configuration")
        self.seriesInstancesText.SetBackgroundColour(wxColour(192, 192, 192))
        self.si_uid_text.SetBackgroundColour(wxColour(192, 192, 192))
        self.study_description_text.SetBackgroundColour(wxColour(192, 192, 192))
        self.referring_physician_text.SetBackgroundColour(wxColour(192, 192, 192))
        self.dimensions_text.SetBackgroundColour(wxColour(192, 192, 192))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: dicomRDRViewFrame.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_6 = wxBoxSizer(wxVERTICAL)
        sizer_2 = wxBoxSizer(wxVERTICAL)
        mdata_sizer = wxFlexGridSizer(3, 2, 4, 4)
        sizer_4 = wxBoxSizer(wxHORIZONTAL)
        sizer_5 = wxBoxSizer(wxHORIZONTAL)
        sizer_3 = wxBoxSizer(wxHORIZONTAL)
        sizer_3.Add(self.label_1_copy_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_3.Add(self.dirname_text, 1, wxRIGHT|wxALIGN_CENTER_VERTICAL, 4)
        sizer_3.Add(self.browse_button, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_3, 1, wxBOTTOM|wxEXPAND, 7)
        sizer_5.Add(self.label_4_copy_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_5.Add(self.si_idx_spin, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_5.Add(self.label_1, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_5.Add(self.seriesInstancesText, 0, wxALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_5, 1, wxBOTTOM|wxEXPAND, 7)
        sizer_4.Add(self.label_5_copy_copy_copy, 0, wxRIGHT|wxALIGN_CENTER_VERTICAL, 3)
        sizer_4.Add(self.si_uid_text, 1, wxALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_4, 1, wxBOTTOM|wxEXPAND, 7)
        mdata_sizer.Add(self.label_9_copy_copy, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        mdata_sizer.Add(self.study_description_text, 1, wxLEFT|wxEXPAND, 2)
        mdata_sizer.Add(self.label_10_copy_copy, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        mdata_sizer.Add(self.referring_physician_text, 1, wxLEFT|wxEXPAND, 2)
        mdata_sizer.Add(self.label_11_copy_copy, 0, wxLEFT|wxRIGHT|wxALIGN_CENTER_VERTICAL, 2)
        mdata_sizer.Add(self.dimensions_text, 1, wxLEFT|wxEXPAND, 2)
        mdata_sizer.AddGrowableCol(1)
        sizer_2.Add(mdata_sizer, 0, wxEXPAND, 7)
        sizer_6.Add(sizer_2, 1, wxALL|wxEXPAND, 7)
        self.viewFramePanel.SetAutoLayout(1)
        self.viewFramePanel.SetSizer(sizer_6)
        sizer_6.Fit(self.viewFramePanel)
        sizer_6.SetSizeHints(self.viewFramePanel)
        sizer_1.Add(self.viewFramePanel, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class dicomRDRViewFrame


