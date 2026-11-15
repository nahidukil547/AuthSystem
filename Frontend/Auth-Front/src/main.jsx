import {StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

// import React from 'react'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App local ='bn-BD'/>
  </StrictMode>,
)
// createRoot.render(
//   <React.StrictMode>
//     <App />
//   </ React.StrictMode>,
//   document.getElementById('root')
// )

// import React from 'react'

// const element = React.createElement('h1',{className:'1st_head', tabIndex:0}, 'Hello world')

// console.log(element)





// import React from "react";
// import {createRoot} from "react-dom/client"

// setInterval(()=>{
//     const element = (
//        <>
//         <h1>Hello World</h1>
//         <span>
//             <strong>Date:</strong>
//             <i>{new Date().toLocaleTimeString()}</i>
//         </span>
        
//        </>
//     )
//     createRoot( document.getElementById('root')).render(element)
// },1000)


