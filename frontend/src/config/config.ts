import dotenv from 'dotenv';
import path from 'path';

dotenv.config({path: path.join(__dirname, '..', '..', '.env')});

/**
 * Config class
 *
 * By default there are empty values because some values might be empty
 */
export class Config {
  /**
   * SERVER OPTIONS
   */
  public static SERVER_URL: string = process.env.SERVER_URL || 'http://localhost:5000';
}
