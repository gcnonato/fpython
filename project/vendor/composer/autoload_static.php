<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInite108460dbbdfef507bebf8b1eefa6d7a
{
    public static $files = array (
        '0e6d7bf4a5811bfa5cf40c5ccd6fae6a' => __DIR__ . '/..' . '/symfony/polyfill-mbstring/bootstrap.php',
        '65fec9ebcfbb3cbb4fd0d519687aea01' => __DIR__ . '/..' . '/danielstjules/stringy/src/Create.php',
    );

    public static $prefixLengthsPsr4 = array (
        'p' => 
        array (
            'project\\' => 8,
        ),
        'S' => 
        array (
            'Symfony\\Polyfill\\Mbstring\\' => 26,
            'Stringy\\' => 8,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'project\\' => 
        array (
            0 => __DIR__ . '/../..' . '/src',
        ),
        'Symfony\\Polyfill\\Mbstring\\' => 
        array (
            0 => __DIR__ . '/..' . '/symfony/polyfill-mbstring',
        ),
        'Stringy\\' => 
        array (
            0 => __DIR__ . '/..' . '/danielstjules/stringy/src',
        ),
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInite108460dbbdfef507bebf8b1eefa6d7a::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInite108460dbbdfef507bebf8b1eefa6d7a::$prefixDirsPsr4;

        }, null, ClassLoader::class);
    }
}
