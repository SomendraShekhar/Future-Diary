import React, { FC, ReactElement } from "react";
import { Box, Container, Grid, Typography, Paper, } from "@material-ui/core";

function Footer() {
    return (
        <Paper sx={{
            marginTop: 'calc(10% + 60px)',
            width: '100%',
            position:"sticky",
            width:"100%",
            top:"96%"
        }} component="footer" square variant="outlined">
            <Container maxWidth="lg">
                <Box
                    sx={{
                        flexGrow: 1,
                        justifyContent: "center",
                        display: "flex",
                    }}
                >
                    <Typography variant="caption" color="initial">
                        Copyright ©2022. [] Limited
                    </Typography>
                </Box>
            </Container>
        </Paper>
    );
};

export default Footer;