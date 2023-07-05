
import { config } from "./configvue.js"

const Core ={
    data: function () {
       return {
        produs:null,
       }

       
    },
    
    delimiters: [
        "--", "--"
    ],

    methods:{
        searchapi:function() {
            fetch(config.URI)
            .then((res) =>res.json())
            .then((pdata) => (this.produs=pdata))
            .catch((e) => console.log(e));
            
            console.log(this);

        },
        searchlocal:function() {
            fetch(config.LOCAL)
            .then((res) =>res.json())
            .then((pdata) => (this.produs=pdata))
            .catch((e) => console.log(e));
            
            console.log(this);

        },

        delimeters : [
            "--", "--"
        ]
    }
};

export {Core};