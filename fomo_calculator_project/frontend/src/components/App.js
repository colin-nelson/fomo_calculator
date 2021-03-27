import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import AboutPage from "./AboutPage";
import FomoPage from "./FomoPage";

export default class App extends Component {
    constructor(props){
        super(props);
    }

    render() {
        return (<div>
                <HomePage />
            </div>
            );    
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);