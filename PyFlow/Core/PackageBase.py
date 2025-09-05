## Copyright 2015-2025 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

from collections import OrderedDict
import os
import importlib.util
import inspect
from typing import Optional

from PyFlow.Core import PinBase
from PyFlow.Core import NodeBase
from PyFlow.Core import FunctionLibraryBase
from PyFlow.UI.UIInterfaces import IDataExporter
from PyFlow.UI.Widgets.PreferencesWindow import CategoryWidgetBase
from PyFlow.UI.Tool.Tool import ToolBase



class PackageBase(object):
    """Class that describes a set of modules that can be plugged into the editor.

    Will be instantiated and used to create registered entities.
    """


    def __init__(self):
        super(PackageBase, self).__init__()
        self._FOO_LIBS = {}
        self._NODES = {}
        self._PINS = {}
        self._TOOLS = OrderedDict()
        self._PREFS_WIDGETS = OrderedDict()
        self._EXPORTERS = OrderedDict()
        self._CUSTOM_PLUGIN_CLASSES = {}

        self._PinsInputWidgetFactory = None
        self._UINodesFactory = None
        self._UIPinsFactory = None

    def analyzePackage(self, packagePath, custom_types: Optional[list[tuple[str, type]]] = None):
        def import_subclasses(directory, base_class):
            subclasses = []
            for filename in os.listdir(directory):
                if filename.endswith(".py") and not filename.startswith("__"):
                    module_name = "PyFlow.Packages."+self.__class__.__name__+"."+os.path.basename(directory)+"."+filename[:-3]
                    file_path = os.path.join(directory, filename)
                    # Dynamically load the module
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for name, obj in inspect.getmembers(module, inspect.isclass):                         
                        # Ensure that the class is defined in this module to avoid imported classes from elsewhere
                        #if inspect.getmodule(obj) == None or inspect.getmodule(obj) == module:		                         		
                        if issubclass(obj, base_class) and obj is not base_class:
                            subclasses.append(obj)
            return subclasses

        def loadPackageElements(packagePath, element, elementDict,classType):
            packageFolders = os.listdir(packagePath)
            if element in packageFolders:
                directory = os.path.join(packagePath, element)
                found_subclasses = import_subclasses(directory, classType)
                for subclass in found_subclasses:
                    if classType == FunctionLibraryBase:
                        elementDict[subclass.__name__] = subclass(self.__class__.__name__, )
                    else:
                        elementDict[subclass.__name__] = subclass

        # initiate custom element store
        if custom_types is None:
            custom_types = []
        for typ in custom_types:
            if typ[0] not in self._CUSTOM_PLUGIN_CLASSES:
                self._CUSTOM_PLUGIN_CLASSES[typ[0]] = {}
        custom_elements = [(typ[0], self._CUSTOM_PLUGIN_CLASSES[typ[0]], typ[1]) for typ in custom_types]
        # Load all elements from the package
        for element in [("FunctionLibraries", self._FOO_LIBS, FunctionLibraryBase),
                        ("Nodes", self._NODES, NodeBase),
                        ("Pins", self._PINS, PinBase),
                        ("Tools", self._TOOLS, ToolBase),
                        ("Exporters", self._EXPORTERS, IDataExporter),
                        ("PrefsWidgets", self._PREFS_WIDGETS, CategoryWidgetBase)] + \
                        custom_elements:
            loadPackageElements(packagePath, element[0], element[1], element[2])
        if os.path.exists(os.path.join(packagePath, "Factories")):
            modPrefix = "PyFlow.Packages."+self.__class__.__name__+".Factories."
            if os.path.exists(os.path.join(packagePath, "Factories", "UIPinFactory.py")):
                spec = importlib.util.spec_from_file_location(modPrefix + "UIPinFactory", os.path.join(packagePath, "Factories", "UIPinFactory.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self._UIPinsFactory = module.createUIPin
            if os.path.exists(os.path.join(packagePath, "Factories", "UINodeFactory.py")):
                spec = importlib.util.spec_from_file_location(modPrefix + "UINodeFactory", os.path.join(packagePath, "Factories", "UINodeFactory.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self._UINodesFactory = module.createUINode
            if os.path.exists(os.path.join(packagePath, "Factories", "PinInputWidgetFactory.py")):
                spec = importlib.util.spec_from_file_location(modPrefix + "PinInputWidgetFactory", os.path.join(packagePath, "Factories", "PinInputWidgetFactory.py"))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                self._PinsInputWidgetFactory = module.getInputWidget

        
    def GetExporters(self):
        """Registered editor data exporters

        :rtype: dict(str, class)
        """
        return self._EXPORTERS

    def GetFunctionLibraries(self):
        """Registered function library instances

        :rtype: dict(str, object)
        """
        return self._FOO_LIBS

    def GetNodeClasses(self):
        """Registered node classes

        :rtype: dict(str, class)
        """
        return self._NODES

    def GetPinClasses(self):
        """Registered pin classes

        :rtype: dict(str, class)
        """
        return self._PINS

    def GetToolClasses(self):
        """Registered tool classes

        :rtype: dict(str, class)
        """
        return self._TOOLS
    
    def PrefsWidgets(self):
        """Registered preferences widgets

        :rtype: dict(str, class)
        """
        return self._PREFS_WIDGETS
    
    def UIPinsFactory(self):
        """Registered ui pin wrappers

        :rtype: function
        """
        return self._UIPinsFactory

    def UINodesFactory(self):
        """Registered ui nodes

        :rtype: function
        """
        return self._UINodesFactory

    def PinsInputWidgetFactory(self):
        """Registered pin input widgets

        :rtype: function
        """
        return self._PinsInputWidgetFactory

    def GetCustomClasses(self, custom_type):
        """Registered custom plugins by their type name.
        
        :rtype: dict[str, class]
        """
        if custom_type not in self._CUSTOM_PLUGIN_CLASSES:
            return {}
        return self._CUSTOM_PLUGIN_CLASSES[custom_type]