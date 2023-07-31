import tkinter as tk
from time import sleep
from typing import Any

from display.Row import DisplayRow
from display.Stage import DisplayStage
from entities.Number import Number
from entities.Row import Row
from entities.Stage import Stage
from matching.DiagonalMatchStrategy import DiagonalMatchStrategy
from matching.EndToStartMatchStrategy import EndToStartMatchStrategy
from matching.HorizontalMatchStrategy import HorizontalMatchStrategy
from matching.VerticalMatchStrategy import VerticalMatchStrategy

STAGE_TOP_X = 10
STAGE_TOP_Y = 50

selectedNumbers = []


def selectNumber(canvas: tk.Canvas, stage: Stage, number: Number):
    global selectedNumbers
    if number.used:
        return

    if len(selectedNumbers) == 0:
        selectedNumbers.append(number)
        number.selected = True

        # TODO optimize by only redrawing the number
        DisplayStage.draw(canvas, STAGE_TOP_X, STAGE_TOP_Y, stage)
    elif len(selectedNumbers) == 1 and number != selectedNumbers[0]:
        if not selectedNumbers[0].canMatch(number):
            selectedNumbers[0].selected = False

            selectedNumbers = [number]
            number.selected = True

            # TODO optimize by only redrawing the number
            DisplayStage.draw(canvas, STAGE_TOP_X, STAGE_TOP_Y, stage)
        else:
            selectedNumbers.append(number)
            number.selected = True

            # TODO optimize by only redrawing the number
            canvas.delete('all')
            DisplayStage.draw(canvas, STAGE_TOP_X, STAGE_TOP_Y, stage)

            sleep(.2)

            sourcePoint = selectedNumbers[0].position
            destinyPoint = selectedNumbers[1].position
            if HorizontalMatchStrategy(stage).canMatch(sourcePoint, destinyPoint) or \
                    VerticalMatchStrategy(stage).canMatch(destinyPoint, sourcePoint) or \
                    DiagonalMatchStrategy(stage).canMatch(sourcePoint, destinyPoint) or \
                    EndToStartMatchStrategy(stage).canMatch(sourcePoint, destinyPoint):

                for number in selectedNumbers:
                    number.use()
                    # TODO calculate points

                selectedNumbers = []

                rowsToCheck = list({sourcePoint.row, destinyPoint.row})
                for idx in range(len(rowsToCheck)):
                    rowIndex = rowsToCheck[idx]
                    row = stage.rows[rowIndex]
                    if row.isComplete():
                        # TODO calculate points
                        stage.rows.pop(rowIndex)
                        for rowBelowIndex in range(rowIndex, len(stage.rows)):
                            for number in stage.rows[rowBelowIndex].numbers:
                                number.position.row -= 1

                            # Update the rowsToCheck if one of its rows was updated
                            if rowBelowIndex in rowsToCheck:
                                rowsToCheck[rowsToCheck.index(rowBelowIndex)] -= 1

                # TODO check if game ended. If so, spawn a new stage

                # TODO optimize by only redrawing the number. Don't forget to draw on top of deleted rows
                canvas.delete('all')
                DisplayStage.draw(canvas, STAGE_TOP_X, STAGE_TOP_Y, stage)

            else:
                selectedNumbers[0].selected = False
                selectedNumbers[1].selected = False

                # TODO optimize by only redrawing the number
                canvas.delete('all')
                DisplayStage.draw(canvas, STAGE_TOP_X, STAGE_TOP_Y, stage)


def numberCanvasOnClick(event: Any, canvas: tk.Canvas, stage: Stage):
    row = DisplayStage.getSelectedRow(event.y - STAGE_TOP_Y, stage)
    if row is None:
        return

    number = DisplayRow.getSelectedNumber(event.x - STAGE_TOP_X, row)
    if number is None:
        return

    selectNumber(canvas, stage, number)

    # TODO optimize by only redrawing the number
    canvas.delete('all')
    DisplayStage.draw(canvas, STAGE_TOP_X, STAGE_TOP_Y, stage)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Number Match')

    # TODO resizing
    window.resizable(False, False)

    # Stage
    initialStage = Stage.generate()

    # Number canvas
    numberCanvas = tk.Canvas(window, width=290, height=560, bg='white')
    numberCanvas.bind('<Button-1>', lambda event: numberCanvasOnClick(event, numberCanvas, initialStage))
    DisplayStage.draw(numberCanvas, STAGE_TOP_X, STAGE_TOP_Y, initialStage)

    numberCanvas.pack()
    window.mainloop()
