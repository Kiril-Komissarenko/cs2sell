import {LoginSession, EAuthTokenPlatformType} from 'steam-session';
import SteamTotp from 'steam-totp';

async function mains(){
    let session = new LoginSession(EAuthTokenPlatformType.SteamClient);

    session.startWithCredentials({
        accountName: nick,
        password: pass
    })

}

async function getPassAndAccountName(){

}

async function getSteamGuardCode(accountName){
    var sharedSecret = getSharedSecret();
    var code = SteamTotp.generateAuthCode(sharedSecret);
    
    return code;
}

async function getSharedSecret(accountName){
    var path = await getMaFilePath(accountName);
    var resp = await fs.readFile(path);
    var json = await resp.json();
    console.log(json);
    console.log(typeof json);
}

async function getMaFilePath(accountName){
    return "C:/Users/ki/Desktop/cs2sell/data/maFiles/aaronflux514.maFile"
}

getSharedSecret("aaronflux514");
