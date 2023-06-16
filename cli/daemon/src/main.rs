use std::{
    fs::File, io::Write, sync::mpsc::channel as CreateMPSC, sync::mpsc::Sender as MPSCSENDER,
    thread::spawn as SpawnThread,
};

use reqwest::blocking as FETCH;

type LPCSTR = str;
type LPWSTR = [u8];
type LPSTR = String;
type INT = isize;
struct HINSTANCE;

const FETCH_SRC: &'static LPCSTR = "127.0.0.1:3131/ph/html";

fn FetchHeadlines(_url: &LPCSTR, sender: MPSCSENDER<Vec<LPSTR>>) {
    let response = FETCH::get(FETCH_SRC).unwrap();
    let headline = response
        .text()
        .unwrap()
        .lines()
        .map(String::from)
        .collect::<Vec<LPSTR>>();
    sender.send(headline).unwrap();
}

fn Driver(tx: MPSCSENDER<Vec<LPSTR>>) {
    // Spawn a thread to fetch the headlines.
    SpawnThread(|| FetchHeadlines(FETCH_SRC, tx));
}

fn WinMain(
    _hInstance: HINSTANCE,
    _hPrevInstance: HINSTANCE,
    _lpCmdLine: &[u8],
    _nCmdShow: INT,
) -> INT {
    // Create a channel to send the headlines to the driver.
    let (tx, rx) = CreateMPSC();

    // Start the driver.
    Driver(tx);

    // Read the headlines from the driver and write them to the MOTD file.
    let mut motd = File::create("/etc/motd").unwrap();
    let res = rx.recv().unwrap().into_iter().map(|line| {
        match motd.write_all(line.bytes().collect::<Vec<u8>>().as_slice()) {
            Ok(_) => 0,
            Err(_) => 1,
        }
    });

    // Exit with a status code indicating failures
    res.sum::<INT>() as INT
}

fn main() {
    std::process::exit(WinMain(HINSTANCE, HINSTANCE, b"", 0) as i32);
}
