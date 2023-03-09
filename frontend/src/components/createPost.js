import { Box, Container, Button, TextField } from '@material-ui/core';
import React, { Component } from 'react';

const renderTextField = ({
    input,
    label,
    meta: {
        touched,
        error
    },
    ...custom
}) => (<TextField
    hintText={label}
    floatingLabelText={label}
    errorText={touched && error}
    {...input}
    {...custom} />)
function createPost() {

    return (
        <div className="row ">
            <div className="col-md-6 col-md-offset-3">
                <h1>Form Example</h1>
                <h3>MaterialUiForm</h3>
                <form>
                    <div>
                        <TextField name="firstName" component={renderTextField} label="First Name" />
                    </div>
                    <div>
                        <TextField name="lastName" component={renderTextField} label="Last Name" />
                    </div>
                    <div>
                        <TextField name="email" component={renderTextField} label="Email" />
                    </div>
                    <div>
                        <TextField
                            name="notes"
                            component={renderTextField}
                            label="Notes"
                            multiLine={true}
                            rows={2} />
                    </div>
                    <Button onClick={handleOpenCategoryMenu} title="submit form" ></Button>
                </form>
            </div>
        </div>
    );
}

export default createPost