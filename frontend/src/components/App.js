import React, { Component } from "react";
import { render } from "react-dom";
import Home  from "./home.js";

// export default class App extends Component {
//   constructor(props) {
//     super(props);
//   }

//   render() {
//     return (
//         <Home />
//     );
//   }
// }

function App (){
  return (
    <Home />
  );
}

export default App;
const appDiv = document.getElementById("app");
render(<App />, appDiv);