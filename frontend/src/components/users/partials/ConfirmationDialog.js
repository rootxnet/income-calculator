import React from "react";
import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import Paper from "@material-ui/core/Paper";
import {DialogTitle, IconButton,} from "@material-ui/core";
import CloseIcon from "@material-ui/icons/Close";

export const ConfirmationDialog = ({
                                     onClose,
                                     open,
                                     message,
                                     rightBtnText,
                                     success
                                   }) => {


  const handleClose = (redirect = false) => {
    onClose(redirect);
  };

  const splitText = (text) => {
    return text.split("\n").map(str => <div key={str}>{str}</div>)
  }

  return (
    <Dialog onClose={() => handleClose()} open={open} fullWidth={true} className="medium-width-modal">
      <Paper className="column">
        <IconButton className="close-btn" onClick={() => handleClose()}>
          <CloseIcon/>
        </IconButton>
        <DialogTitle className={success ? "dialog-title" : "dialog-title red-title"}>
          {splitText(message)}
        </DialogTitle >
        <div className="column column-buttons">
          <Button
            className="medium-width-input"
            variant="contained"
            color="primary"
            onClick={() => handleClose(true)}>
            {rightBtnText}
          </Button>
          <Button
            className="medium-width-input"
            onClick={() => handleClose(false)}
          >
            Return To Dashboard
          </Button>
        </div>
      </Paper>
    </Dialog>
  );
}
