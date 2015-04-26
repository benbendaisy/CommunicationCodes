package com.example.other;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Formatter;

/**
 * Created by benbendaisy on 4/25/15.
 */
public class Sha1Sample {
    private static String encryptPasswordSha1(String password) {
        String sha1 = "";
        try {
            MessageDigest crypt = MessageDigest.getInstance("SHA-1");
            crypt.reset();
            crypt.update(password.getBytes("UTF-8"));
            sha1 = byteToHex(crypt.digest());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return sha1;
    }

    private static String encryptPasswordSha256(String password) {
        String sha1 = "";
        try {
            MessageDigest crypt = MessageDigest.getInstance("SHA-256");
            crypt.reset();
            crypt.update(password.getBytes("UTF-8"));
            sha1 = byteToHex(crypt.digest());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        return sha1;
    }

    private static String byteToHex(final byte[] hash) {
        Formatter formatter = new Formatter();
        for (byte b : hash) {
            formatter.format("%02x", b);
        }
        String result = formatter.toString();
        formatter.close();
        return result;
    }

    private static String byteToHexI(final byte[] hash) {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < hash.length; i++) {
            sb.append(Integer.toString((hash[i] & 0xff) + 0x100, 16).substring(1));
        }
        return sb.toString();
    }

    private static String byteToHexII(final byte[] hash) {
        StringBuffer hexString = new StringBuffer();
        for (int i = 0; i < hash.length; i++) {
            hexString.append(Integer.toHexString(0xFF & hash[i]));
        }
        return hexString.toString();
    }

    public static void main(String[] args) {
        String pwd = "abcdefgh123456";
        String epwd = encryptPasswordSha1(pwd);
        System.out.println(epwd);

        epwd = encryptPasswordSha256(pwd);
        System.out.println(epwd);
        //need guava dependency
        //System.out.println(Hashing.sha1().hashString( pwd, Charsets.UTF_8 ).toString());
        System.out.println(epwd.length());
    }

    private void hashFile(String path) {
        MessageDigest md = null;
        try {
            md = MessageDigest.getInstance("SHA-256");
            FileInputStream fis = new FileInputStream(path);
            byte[] dataBytes = new byte[1024];
            int nread = 0;
            while ((nread = fis.read(dataBytes)) != -1) {
                md.update(dataBytes, 0, nread);
            }
            byte[] mdbytes = md.digest();
            //convert the byte to hex format method 1
            System.out.println("Hex format : " + byteToHexI(mdbytes));
            //convert the byte to hex format method 2
            System.out.println("Hex format : " + byteToHexII(mdbytes));
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (FileNotFoundException fe) {
            fe.printStackTrace();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
