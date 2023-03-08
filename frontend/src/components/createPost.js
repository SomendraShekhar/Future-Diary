import { Box, Container } from '@material-ui/core';
import React ,{ Component } from 'react';

export default class CreatePost extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (
            <Box>
                <Container>
                <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                
                </Container>
            </Box>
        
        );
    }
}