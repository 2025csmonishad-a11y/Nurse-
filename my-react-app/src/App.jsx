import React,{useState} from "react"
import "./App.css"
import "bootstrap/dist/css/bootstrap.min.css"
function Display({Filename,Size}){
  return(
    <>
    <img src={Filename} width={Size} title="nature image"/>
    </>
  )
}
function Mydata(){
  return(
    <>
       <h1>welcome to nie</h1><br/>
       <h2>my name is xyz</h2><br/>
       <h3>i train in full stack development</h3>
       <h4 title="hello">i live in banglore</h4>
    </>
  )
}
export default function main(){
  const[name,setName]=useState('')
  const[pwd,setPwd]=useState("")
  function Validate(){
    if(name=="kushal"&&pwd=="1029")
      alert("valid user")
    else
      alert("Invalid user")
  }
  function Buttonclicked(){
    alert("do you want to procced in new webpage")
  }
  function Displaytext(){
    alert("entered name:"+name)
  }
  return(
    <>
    
    <Mydata / >
    <div>
    <a href="https://nodejs.org/en/download" target="_blank"><Display Filename="red.jpg" Size={300}/>&nbsp;</a>
    <Display Filename="vin2.jpg" Size={300} />&nbsp;
    </div>
    <a href="https://nodejs.org/en/blog/release/v22.0.0" target="_blank"><button className="btn btn-primary" onClick={Buttonclicked} style={{width:"1000px"}}>nodejs</button></a>
    <br/>
    <a href="https://nodejs.org/en/blog/release/v22.0.0" target="_blank"><button className="btn btn-secondary" onClick={Buttonclicked} style={{width:"200px"}}>nodejs</button></a>
    <br/>
    <a href="https://nodejs.org/en/blog/release/v22.0.0" target="_blank"><button className="btn btn-danger" onClick={Buttonclicked} style={{width:"200px"}}>nodejs</button></a>
    <br/>
    <a href="https://nodejs.org/en/blog/release/v22.0.0" target="_blank"><button className="btn btn-info" onClick={Buttonclicked} style={{width:"200px"}}>nodejs</button></a>
    <br/>
    <a href="https://nodejs.org/en/blog/release/v22.0.0" target="_blank"><button className="btn btn-primary" onClick={Buttonclicked} style={{width:"200px"}}>nodejs</button></a>
    <br/>
    <div>
    <p>enter your name:</p>
    <input type="text" className="from-control" onChange={(e) => setName(e.target.value)} style={{width:"200px"}}/>&nbsp;
    <button className="btn btn-primary" onClick={Displaytext} style={{width:"200px"}}>Click</button>
    </div>
      <form>
        <h1>login form</h1>
        UserId:
        <input type="text" className="form-control" onChange={(e) => setName(e.target.value)} style={{width:"200px"}}/><br/>
        password:
        <input type="text" className="form-control" onChange={(e) => setPwd(e.target.value)} style={{width:"200px"}}/><br/>
      <button onClick={Validate}>Login</button>
      </form>
    </>
  )
}
