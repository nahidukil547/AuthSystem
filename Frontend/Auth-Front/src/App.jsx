// import { useState } from 'react'
import ClockComp from "./components/Login"
import { useEffect, useState } from "react"


function App({ local }) {
  // const [count, setCount] = useState(0)
  console.log('Hello World') // console ta 2 bar keno hocce 

  const [time, setTime] = useState(new Date())  

  useEffect (()=>{
    const intervalId = setInterval(() =>{
      setTime(new Date())
    },1000)
    return ()=> clearInterval(intervalId)
  },[])

  return (
    <>
     <div>Hello World</div>
     <p>
      <strong>Date: </strong>
      <i>
        {time.toLocaleTimeString(local)}
      </i>
     </p>
      {ClockComp.print()}
    </>
  )
}

export default App
