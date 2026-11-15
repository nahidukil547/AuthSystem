import { Component } from "react"

class Clock extends Component {
    render(){
        return(
                <h1>
                    This is from Clock located in {this.props.area}
                </h1>
            )
    }
}

export default Clock