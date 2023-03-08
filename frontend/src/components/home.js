import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";
import Header from './header';
import Footer from './footer';
import CreatePost from './createPost';
import Post from './posts';
export default class Home extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div>
                <Header />
                <Router>
                    <Switch>
                        <Route exact path='/' component={Post} />
                        <Route path='/createPost' component={CreatePost} />
                    </Switch>
                </Router>
                <Footer />
            </div>
        );
    }
}
