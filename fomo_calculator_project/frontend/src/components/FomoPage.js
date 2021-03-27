import React, { Component } from "react";
import Button from "@material-ui/core/Button"
import Grid from "@material-ui/core/Grid"
import Typography from "@material-ui/core/Typography"
import Textfield from "@material-ui/core/TextField"
import FormHelperText from "@material-ui/core/FormHelperText"
import FormControl from "@material-ui/core/FormControl"
import { Link } from "react-router-dom"
import Radio from "@material-ui/core/Radio"
import RadioGroup from "@material-ui/core/RadioGroup"
import FormControlLabel from "@material-ui/core/FormControlLabel"
import Select from "@material-ui/core/Select"
import InputLabel from "@material-ui/core/InputLabel"

export default class FomoPage extends Component {
    constructor(props){
        super(props);
        this.state = {
            coin: "bitcoin",
            currency: "usd",
            date: "2013-04-27",
            amount: 1,
            fomo: 1
        };
        this.handleAmountChange = this.handleAmountChange.bind(this)
        this.handleCoinChange = this.handleCoinChange.bind(this)
        this.handleFomoButtonPress = this.handleFomoButtonPress.bind(this)
    };   


handleAmountChange(e) {
    this.setState({
        amount: e.target.value,
    });
}

handleCoinChange(e) {
    this.setState({
        coin: e.target.value
    });
}

handleFomoButtonPress() {
    console.log(this.state)
    alert("Workin on that")
    const calculateFomo = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            coin: this.state.coin,
            currency: this.state.currency,
            date: this.state.date,
            amount: this.state.amount,
            fomo: this.state.fomo
        }),
    }
    fetch('/api/fomo-view', calculateFomo)
    .then((response) => response.json())
    .then((data) => console.log(data));
}

    render() { 
        
        return( 
        <Grid container spacing={1}>
            <Grid item xs={12} align="center">
                <Typography component='h4' variant='h4'>
                    FOMO
                </Typography>
            </Grid>

            <Grid item xs={12} align="center">
                <FormControl component="fieldset">
                    <FormHelperText>
                        <div align="center">Calculate your FOMO!!</div>
                    </FormHelperText>
                    <RadioGroup row defaultValue="true">
                        <FormControlLabel value="true" control={<Radio color="primary" />} label="Text" labelPlacement="botom"/>
                        <FormControlLabel value="false" control={<Radio color="secondary" />} label="Graph" labelPlacement="botom"/>
                    </RadioGroup>
                </FormControl>
            </Grid>

            <Grid item xs={12} align="center">
                <FormControl>
                    <Textfield 
                        required={true} 
                        type="number"
                        onChange={this.handleAmountChange}
                        defaultValue={1}
                        inputProps={{
                            min: 1,
                            style: {textAlign: "center"}
                        }} 
                        />
                        <FormHelperText>
                            <div align="center">
                                USD spent
                            </div>
                        </FormHelperText>
                </FormControl>
            </Grid>

            <Grid item xs={12} align="center">
                <FormControl variant="outlined">
                    <InputLabel htmlFor="outlined-age-native-simple" onChange={this.handleCoinChange}>Crypto</InputLabel>
                    <Select
                    native
                    label="Crypto"
                    inputProps={{
                        name: 'crypto',
                        id: 'outlined-age-native-simple',
                    }}
                    >
                    <option value={"bitcoin"}>BTC</option>
                    <option value={"ethereum"}>ETH</option>
                    <option value={"cardano"}>ADA</option>
                    </Select>
                </FormControl>
            </Grid>

            <Grid item xs={12} align="center">
                <Button color="primary" variant="contained" onClick={this.handleFomoButtonPress}>
                    Calculate FOMO
                </Button>
            </Grid>            
            <Grid item xs={12} align="center">
                <Button color="secondary" variant="contained" to="/" component={Link}>
                    Back to home
                </Button>
            </Grid>

        </Grid>
        );
    }
}