
// components/Login.jsx
import { Component } from 'react';

// রিয়্যাক্টের Component ক্লাসকে ইনহেরিট (inherit) করতে হবে
class Login extends Component {
    // রিয়্যাক্ট ক্লাস কম্পোনেন্টে রেন্ডারের জন্য render() মেথড বাধ্যতামূলক
    render() {
        return (
            <>
                <h1>
                    This is from Login.jsx
                </h1>
            </>
        );
    }
}

// ক্লাসটি সরাসরি এক্সপোর্ট করতে হবে
export default Login;