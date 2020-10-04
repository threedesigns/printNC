#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
import os

_app = None
_ui  = None

# Global set of event handlers to keep them referenced for the duration of the command
_handlers = []

class Print3DPiece():
    def __init__(self, full_path):
        self.full_path = full_path
        self.export = True

    def get_object(self, root):
        component = root
        try:
            for component_name in self.full_path:
                try:
                    component = component.occurrences.itemByName(component_name).component
                except AttributeError:
                    obj = component.bRepBodies.itemByName(component_name)
                    if obj is None:
                        raise KeyError("")
                    component=obj
        except:
            raise KeyError(f"{component_name} in {self.full_path} not found")
        return component

    def export_stl(self, exportMgr, root, path):
        stlOptions = exportMgr.createSTLExportOptions(self.get_object(root))
        stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
        stlOptions.filename = path
        exportMgr.execute(stlOptions)

pieces = {
    'Assembly Tools': {
        '1 - Y Frame Marker': Print3DPiece(['Assembly Tools:1','1 - Y Frame Marker:1']),
        '2 - X Frame Marker': Print3DPiece(['Assembly Tools:1','2 - X Frame Marker:1']),
        '3 - Y Frame Mid Marker': Print3DPiece(['Assembly Tools:1','3 - Y Frame Mid Marker:1']),
        '4 - Y Roller Bottom': Print3DPiece(['Assembly Tools:1','4 - Y Roller Bottom:1']),
        '5 - Y Roller Top': Print3DPiece(['Assembly Tools:1','5 - Y Roller Top:1']),
        '6 - X-Gantry': Print3DPiece(['Assembly Tools:1','6 - X Gantry:1']),
        '6A - X-Gantry Part 2': Print3DPiece(['Assembly Tools:1','6A - X Gantry Part 2:1']),
        '7 - X Axis Roller': Print3DPiece(['Assembly Tools:1','7 - X Axis Roller:1']),
        '8 - Z Face Rail Top': Print3DPiece(['Assembly Tools:1','8 - Z Face/Rail Top:1']),
        '9 - Z Face Roll Bottom': Print3DPiece(['Assembly Tools:1','9 - Z Face/Rail Bottom:1']),
        'Centre Line Marker': Print3DPiece(['Assembly Tools:1','Centre Line Marker:1'])
    },
    'X-Y Axis': {
        'Ball Screw Face Plate Front': Print3DPiece([
            'Y Axis:1',
            'Ball Screw Mount:1',
            'Ball Screw Face Plate:1',
            'Ball Screw Face Plate']),
        'Ball Screw Face Plate Rear': Print3DPiece([
            'Y Axis:1',
            'Ball Screw Mount:1',
            'Ball Screw Face Plate:1',
            'Ball Screw Face Plate (2)']),
        'Ball Screw Face Plate w EndStop': Print3DPiece(['Z Axis:1','Ball Screw Face Plate (1):1', 'Ball Screw Face Plate']),
        'BF12 Mount': Print3DPiece(['Y Axis:1','BF12 Mount X :1', 'Body1']),
        'BK12 Mount': Print3DPiece(['Y Axis:1','BK12 Mount:1', 'Mount']),
        'Tensioner Brace': Print3DPiece(['X Axis:1','Nema 17:1', 'Dual Mount:1', 'Tensioner (1):1', 'Brace:1', 'Body1']),
        'Tensioner': Print3DPiece(['X Axis:1','Nema 17:1', 'Dual Mount:1', 'Tensioner (1):1', 'Tensioner']),
        'X-Axis NEMA 17 Mount': Print3DPiece(['X Axis:1','Nema 17:1', 'Dual Mount:1', 'Riser (1)']),
        'XY-Axis NEMA 23 Mount': Print3DPiece(['Y Axis:1','NEMA23:1', 'Base']),
        'Y-Axis NEMA 17 Mount': Print3DPiece(['Y Axis:1','NEMA17 (1):1', 'Mount']),
    },
    'Z Axis': {
        'T8 Riser': Print3DPiece(['Z Axis:1','T8 Riser:1', 'Riser']),
        'Z-Axis NEMA 17 Mount': Print3DPiece(['Z Axis:1','Nema 17 Mount (1):1', 'Nema 17 Mount:1', 'Mount']),
        'Z-Axis NEMA 23 Mount': Print3DPiece(['Z Axis:1','Nema 23:1', 'Body1']),
    },
    'Aesthetic': {
        'End Cover': Print3DPiece(['Z Axis:1','Cover Plate:1', 'Body1']),
    }
}

box_profiles = {
    '3x2x_125_w_25_Radius': {
        'Tall': '3 in',
        'Narrow': '2 in',
        'Thickness': '.125 in',
        'Radius': '.25 in'
    },
    '3x2x1_8 Square': {
        'Tall': '3 in',
        'Narrow': '2 in',
        'Thickness': '.125 in',
        'Radius': '0'
    },
    '75x50x3 w 6mm Radius': {
        'Tall': '75 mm',
        'Narrow': '50 mm',
        'Thickness': '3.175 mm',
        'Radius': '5.6 mm'
    },
    '75x50x3 Square': {
        'Tall': '75 mm',
        'Narrow': '50 mm',
        'Thickness': '3.175 mm',
        'Radius': '0'
    },    
    '80x50x3 w 6mm Radius': {
        'Tall': '80 mm',
        'Narrow': '50 mm',
        'Thickness': '3.175 mm',
        'Radius': '5.6 mm'
    },
    '80x50x3 Square': {
        'Tall': '80 mm',
        'Narrow': '50 mm',
        'Thickness': '3.175 mm',
        'Radius': '0'
    },
}

class MyCommandInputChangedHandler(adsk.core.InputChangedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            eventArgs = adsk.core.InputChangedEventArgs.cast(args)
            inputs = eventArgs.inputs
            cmdInput = eventArgs.input
            if cmdInput.id in pieces.keys():
                cmdInput.isExpanded = not cmdInput.isExpanded
                for key, item in pieces[cmdInput.id].items():
                    item.export = cmdInput.isEnabledCheckBoxChecked
                for item in cmdInput.children:
                    item.value = cmdInput.isEnabledCheckBoxChecked
                return
            elif cmdInput.id == 'folderChange':
                folder_dialog = _ui.createFolderDialog()
                folder_dialog.title="Choose root path for export"
                if folder_dialog.showDialog() == 1:
                    return
                rootFolder = folder_dialog.folder
                savefolder_input = cmdInput.parentCommandInput.children.itemById('savefolder')
                savefolder_input.text = rootFolder

            elif cmdInput.id == 'export' or cmdInput.id == 'exportcurrent':
                tabChildren = cmdInput.parentCommandInput.children
                savefolder_input = tabChildren.itemById('savefolder')
                rootFolder = savefolder_input.text
                if not os.path.exists(rootFolder):
                    _ui.messageBox('Root folder does not exist or needs to be selected')
                    return
                design = adsk.fusion.Design.cast(_app.activeProduct)
                exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
                if not design:
                    ui.messageBox('No active Fusion 360 design', 'No Design')
                    return
                rootComp = design.rootComponent
                if cmdInput.id == 'exportcurrent':
                    for folder, components in pieces.items():
                        cur_dir = os.path.join(rootFolder, folder)
                        if not os.path.exists(cur_dir):
                            os.mkdir(cur_dir)
                        for comp_name, comp in components.items():
                            filename = os.path.join(cur_dir, comp_name+".stl")
                            if comp.export:
                                comp.export_stl(exportMgr, rootComp, filename)
                    return

                narrowParam = design.allParameters.itemByName('extrusionNarrow')
                tallParam = design.allParameters.itemByName('extrusionTall')
                thicknessParam = design.allParameters.itemByName('extrusionThickness')
                radiusParam = design.allParameters.itemByName('extrusionRadius')
                for profile_name, profile_dim in box_profiles.items():
                    profile_checkbox = tabChildren.itemById(profile_name)
                    if profile_checkbox.value:
                        profileFolder = os.path.join(rootFolder, profile_name)
                        if not os.path.exists(profileFolder):
                            os.mkdir(profileFolder)
                        narrowParam.expression = profile_dim['Narrow']
                        tallParam.expression = profile_dim['Tall']
                        thicknessParam.expression = profile_dim['Thickness']
                        radiusParam.expression = profile_dim['Radius']
                        # adsk.doEvents()
                        for folder, components in pieces.items():
                            cur_dir = os.path.join(profileFolder, folder)
                            if not os.path.exists(cur_dir):
                                os.mkdir(cur_dir)
                            for comp_name, comp in components.items():
                                filename = os.path.join(cur_dir, comp_name+".stl")
                                if comp.export:
                                    comp.export_stl(exportMgr, rootComp, filename)
                _ui.messageBox("File Complete")

            elif cmdInput.parentCommandInput is not None:
                if cmdInput.parentCommandInput.id in pieces.keys():
                    folder = pieces[cmdInput.parentCommandInput.id]
                    folder[cmdInput.id].export = cmdInput.isEnabled

        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

# Event handler that reacts to when the command is destroyed. This terminates the script.            
class MyCommandDestroyHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        try:
            # When the command is done, terminate the script
            # This will release all globals which will remove all event handlers
            adsk.terminate()
        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

class MyCommandCreatedHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        global _ui
        try:
            # Get the command that was created.
            # Get the command that was created.
            cmd = adsk.core.Command.cast(args.command)

            # Connect to the command destroyed event.
            onDestroy = MyCommandDestroyHandler()
            cmd.destroy.add(onDestroy)
            _handlers.append(onDestroy)

            # Connect to the input changed event.           
            onInputChanged = MyCommandInputChangedHandler()
            cmd.inputChanged.add(onInputChanged)
            _handlers.append(onInputChanged)    

            # Get the CommandInputs collection associated with the command.
            inputs = cmd.commandInputs

            # Create a tab for output files
            tabCmdInput2 = inputs.addTabCommandInput('tab_1', 'Dim Outputs')
            tab2ChildInputs = tabCmdInput2.children
            tab2ChildInputs.addTextBoxCommandInput(
                'savefolder', 
                'Save Folder', 
                '',
                 2, True)
            tab2ChildInputs.addBoolValueInput('folderChange', 'Change Folder', False)
            
            for profile_name, profile_dims in box_profiles.items():
                checkbox = tab2ChildInputs.addBoolValueInput(profile_name, profile_name, True, '', True)

            tab2ChildInputs.addBoolValueInput('export', 'Export', False)
            tab2ChildInputs.addBoolValueInput('exportcurrent', 'Export Current', False)

            # Create a tab for output files
            tabCmdInput1 = inputs.addTabCommandInput('tab_2', 'STL Outputs')
            tab1ChildInputs = tabCmdInput1.children

            for folder, components in pieces.items():
                categories = tab1ChildInputs.addGroupCommandInput(folder, folder)
                categories.isExpanded = False
                categories.isEnabledCheckBoxDisplayed = True
                groupChildInputs = categories.children
                for comp_name, comp in components.items():
                    checkbox = groupChildInputs.addBoolValueInput(comp_name, comp_name, True, '', True)

        except:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run(context):
    global _app, _ui
    _app = adsk.core.Application.get()
    _ui = _app.userInterface
    try:
        cmdDef = _ui.commandDefinitions.itemById('printNCOutput2')
        # if cmdDef is not None:
        #     cmdDef.deleteMe()
        if not cmdDef:
            cmdDef = _ui.commandDefinitions.addButtonDefinition(
                'printNCOutput2', 
                'Output STL files',
                'Output STL files for PrintNC')
        # Connect to the command created event.
        onCommandCreated = MyCommandCreatedHandler()
        cmdDef.commandCreated.add(onCommandCreated)
        _handlers.append(onCommandCreated)

        cmdDef.execute()
        
        adsk.autoTerminate(False)
    except:
        if _ui:
            _ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
