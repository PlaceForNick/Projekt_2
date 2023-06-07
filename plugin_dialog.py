# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaDialog
                                 A QGIS plugin
 obliczanie odległoćsi oraz pól powierzchni zaznaczonych elementów
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-06
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Adam Sala, Adrian Rykiel
        email                : 123@456.789
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import numpy as np
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import (
  QgsApplication,
  QgsDataSourceUri,
  QgsCategorizedSymbolRenderer,
  QgsClassificationRange,
  QgsPointXY,
  QgsProject,
  QgsExpression,
  QgsField,
  QgsFields,
  QgsFeature,
  QgsFeatureRequest,
  QgsFeatureRenderer,
  QgsGeometry,
  QgsGraduatedSymbolRenderer,
  QgsMarkerSymbol,
  QgsMessageLog,
  QgsRectangle,
  QgsRendererCategory,
  QgsRendererRange,
  QgsSymbol,
  QgsVectorDataProvider,
  QgsVectorLayer,
  QgsVectorFileWriter,
  QgsWkbTypes,
  QgsSpatialIndex,
  QgsVectorLayerUtils
)

from qgis.core.additions.edit import edit

from qgis.PyQt.QtGui import (
    QColor,
)

from qgis.core import Qgis

from qgis.core import (
    QgsMessageLog,
    QgsGeometry,
)

from qgis.gui import (
    QgsMessageBar,
)

from qgis.PyQt.QtWidgets import (
    QSizePolicy,
    QPushButton,
    QDialog,
    QGridLayout,
    QDialogButtonBox,
)

from qgis.utils import iface
from PyQt5 import QtGui
# from PyQt5.QtCore import Qt

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'plugin_dialog_base.ui'))


class WtyczkaDialog( QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.textBrowser_info_zwrotne.setText('Zaznacz 2 elementy, aby móc obliczyć odległość.\nZaznacz minimum 3 elementy aby móc obliczyć pole powierzchni.')
        self.pushButton_obl_odleglosc.clicked.connect(self.oblicz_odleglosc)
        self.pushButton_obl_pole.clicked.connect(self.oblicz_pole)
        
        self.kreska = '-'*46
        
    def oblicz_odleglosc(self):
        
        zaznaczone_elementy = self.mMapLayerComboBox_wybor_warstwy.currentLayer().selectedFeatures()
        liczba_zaznaczonych_elementow = len(zaznaczone_elementy)
        
        # self.textBrowser_info_zwrotne.append(f'{self.kreska}\nLiczba zaznaczonych elementów wynosi:\n{liczba_zaznaczonych_elementow}')
        
        # "layer" is a QgsVectorLayer instance
        layer = self.mMapLayerComboBox_wybor_warstwy.currentLayer()

        X = []
        Y = []
        selection = layer.selectedFeatures()
        
        if liczba_zaznaczonych_elementow == 2:
            
            for feature in selection:
                geom = feature.geometry()
                y = geom.asPoint().y()
                x = geom.asPoint().x()
                X.append(x)
                Y.append(y)   
            odl = np.sqrt((X[1] - X[0])**2 + (Y[1] - Y[0])**2)
            
            self.textBrowser_info_zwrotne.append(f'{self.kreska}\nObliczona odległość wynosi:\n{odl:0.3f} m')
            self.__wypluwacz('Success', f'Obliczono odległość: {odl:0.3f} m')
            
        elif liczba_zaznaczonych_elementow < 2:
            
            self.textBrowser_info_zwrotne.append(f'{self.kreska}\nZaznaczono za małą ilość elementów!\nAby skorzystać z tej funkcji musisz zaznaczyć dokładnie 2 elementy!')
            self.__wypluwacz('Warning', 'Zaznaczono niepoprawną ilość elementów!')
        
        else:
            
            self.textBrowser_info_zwrotne.append(f'{self.kreska}\nZaznaczono za dużą ilość elementów!\nAby skorzystać z tej funkcji musisz zaznaczyć dokładnie 2 elementy!')
            self.__wypluwacz('Warning', 'Zaznaczono niepoprawną ilość elementów!')
            
    def oblicz_pole(self):
        
        zaznaczone_elementy = self.mMapLayerComboBox_wybor_warstwy.currentLayer().selectedFeatures()
        liczba_zaznaczonych_elementow = len(zaznaczone_elementy)
        
        # self.textBrowser_info_zwrotne.append(f'{self.kreska}\nLiczba zaznaczonych elementów wynosi:\n{liczba_zaznaczonych_elementow}')
        
        # "layer" is a QgsVectorLayer instance
        layer = self.mMapLayerComboBox_wybor_warstwy.currentLayer()

        X = []
        Y = []
        selection = layer.selectedFeatures()
        
        if liczba_zaznaczonych_elementow > 2:
            
            for feature in selection:
                geom = feature.geometry()
                y = geom.asPoint().y()
                x = geom.asPoint().x()
                X.append(x)
                Y.append(y)   
            pole =  0.5*np.abs(np.dot(X,np.roll(Y,1))-np.dot(Y,np.roll(X,1)))
            
            self.textBrowser_info_zwrotne.append(f'{self.kreska}\nObliczone pole powierzchni wynosi:\n{pole:0.3f} m2')
            self.__wypluwacz('Success', f'Obliczono pole powierzchni: {pole:0.3f} m2')

        else:
            
            self.textBrowser_info_zwrotne.append(f'{self.kreska}\nZaznaczono za małą ilość elementów!\nAby skorzystać z tej funkcji musisz zaznaczyć co najmniej 3 elementy!')
            self.__wypluwacz('Warning', 'Zaznaczono niepoprawną ilość elementów!')
            
    def __wypluwacz(self, typ, tekst):
        
        if typ == 'Info':
            poziom = Qgis.Info
        elif typ == 'Error':
            poziom = Qgis.Critical
        elif typ == 'Warning':
            poziom = Qgis.Warning 
        else: 
            poziom = Qgis.Success
            
        widget = iface.messageBar().createMessage(typ, tekst)
        button = QPushButton(widget)
        button.setText("Ok")
        # button.pressed.connect(WtyczkaDialog.show()) 
        widget.layout().addWidget(button)
        iface.messageBar().pushWidget(widget, level=poziom, duration=5)
        
